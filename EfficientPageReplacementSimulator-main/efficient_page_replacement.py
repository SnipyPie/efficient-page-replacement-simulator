#!/usr/bin/env python3
"""
Page Replacement Algorithm Simulator

This script provides an interactive Streamlit application to simulate 
and compare different page replacement algorithms.
"""

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from collections import OrderedDict

class PageReplacement:
    @staticmethod
    def fifo_algorithm(pages, total_frames):
        """(FIFO) Page Replacement Algo"""
        queue_fifo = []
        page_faults = 0
        page_hits = 0
        steps = []

        for page in pages:
            if page in queue_fifo:
                page_hits += 1
                steps.append({
                    'page': page, 
                    'status': 'Hit', 
                    'memory': queue_fifo.copy()
                })
            else:
                page_faults += 1
                if len(queue_fifo) < total_frames:
                    queue_fifo.append(page)
                else:
                    queue_fifo.pop(0)
                    queue_fifo.append(page)
                
                steps.append({
                    'page': page, 
                    'status': 'Miss', 
                    'memory': queue_fifo.copy()
                })

        return page_faults, page_hits, steps

    @staticmethod
    def lru_algorithm(pages, total_frames):
        """(LRU) Page Replacement Algo"""
        page_cache = OrderedDict()
        page_faults = 0
        page_hits = 0
        steps = []

        for page in pages:
            if page in page_cache:
                page_hits += 1
                # Move the page to the end to show it's most recently used
                page_cache.move_to_end(page)
                steps.append({
                    'page': page, 
                    'status': 'Hit', 
                    'memory': list(page_cache.keys())
                })
            else:
                page_faults += 1
                if len(page_cache) >= total_frames:
                    # Remove the least recently used item (first item)
                    page_cache.popitem(last=False)
                
                page_cache[page] = None
                steps.append({
                    'page': page, 
                    'status': 'Miss', 
                    'memory': list(page_cache.keys())
                })

        return page_faults, page_hits, steps

    @staticmethod
    def optimal_algorithm(pages, total_frames):
        """Optimal Page Replacement Algo"""
        memory_store = []
        page_faults = 0
        page_hits = 0
        steps = []

        for i, page in enumerate(pages):
            if page in memory_store:
                page_hits += 1
                steps.append({
                    'page': page, 
                    'status': 'Hit', 
                    'memory': memory_store.copy()
                })
            else:
                page_faults += 1
                
                if len(memory_store) < total_frames:
                    memory_store.append(page)
                else:
                    # Find page to replace based on future references
                    future_refs = {}
                    for mem_page in memory_store:
                        try:
                            future_refs[mem_page] = pages[i+1:].index(mem_page)
                        except ValueError:
                            future_refs[mem_page] = len(pages)
                    
                    # Replace the page that will be used furthest in the future
                    replace_page = max(future_refs, key=future_refs.get)
                    memory_store[memory_store.index(replace_page)] = page

                steps.append({
                    'page': page, 
                    'status': 'Miss', 
                    'memory': memory_store.copy()
                })

        return page_faults, page_hits, steps

def main():
    # Page Config
    st.set_page_config(
        page_title="Page Replacement Algorithm Simulator", 
        page_icon="💾", 
        layout="wide"
    )

    # Title
    st.title("💾 Page Replacement Algorithm Simulator")
    st.markdown("""
    ### Explore Different Page Replacement Strategies
    Compare FIFO, LRU, and Optimal algorithms to understand memory management techniques.
    """)

    # Sidebar Inputs
    st.sidebar.header("🔧 Simulation Parameters")
    
    # Ref String Input
    default_ref_string = "7 0 1 2 0 3 4 2 3 0 3 2"
    reference_string = st.sidebar.text_input(
        "Enter Reference String", 
        value=default_ref_string
    )

    # Num of Frames
    num_frames = st.sidebar.slider(
        "Number of Memory Frames", 
        min_value=1, 
        max_value=10, 
        value=3
    )

    # Algo Selection
    algorithms = st.sidebar.multiselect(
        "Select Algorithms to Simulate",
        ["FIFO", "LRU", "Optimal"],
        default=["FIFO", "LRU", "Optimal"]
    )

    # Convert ref string to list of int
    try:
        pages = list(map(int, reference_string.split()))
    except ValueError:
        st.error("Please enter a valid space-separated list of integers.")
        return

    # Run Simulation Button
    if st.sidebar.button("🚀 Run Simulation"):
        # Results Container
        results_container = st.container()
        
        with results_container:
            # Performance Metrics
            st.subheader("📊 Performance Metrics")
            
            # Prepare results DataFrame
            results_data = []
            
            # Detailed Steps Storage
            detailed_steps = {}

            # Run selected algorithms
            for algo in algorithms:
                if algo == "FIFO":
                    page_faults, page_hits, steps = PageReplacement.fifo_algorithm(pages, num_frames)
                elif algo == "LRU":
                    page_faults, page_hits, steps = PageReplacement.lru_algorithm(pages, num_frames)
                else:  # Optimal
                    page_faults, page_hits, steps = PageReplacement.optimal_algorithm(pages, num_frames)
                
                # Calculate metrics
                total_pages = len(pages)
                hit_ratio = page_hits / total_pages * 100
                fault_ratio = page_faults / total_pages * 100
                
                # Store results
                results_data.append({
                    'Algorithm': algo,
                    'Page Faults': page_faults,
                    'Page Hits': page_hits,
                    'Hit Ratio (%)': round(hit_ratio, 2),
                    'Fault Ratio (%)': round(fault_ratio, 2)
                })
                
                # Store detailed steps
                detailed_steps[algo] = steps

            # Display Results Table
            results_df = pd.DataFrame(results_data)
            st.table(results_df)

            # Visualization Column
            col1, col2 = st.columns(2)

            # Bar Chart for Page Faults
            with col1:
                st.subheader("Page Faults Comparison")
                plt.figure(figsize=(8, 5))
                plt.bar(results_df['Algorithm'], results_df['Page Faults'])
                plt.title("Page Faults by Algorithm")
                plt.xlabel("Algorithm")
                plt.ylabel("Number of Page Faults")
                st.pyplot(plt)
                plt.close()

            # Pie Chart for Hit Ratio
            with col2:
                st.subheader("Hit Ratio Comparison")
                plt.figure(figsize=(8, 5))
                plt.pie(
                    results_df['Hit Ratio (%)'], 
                    labels=results_df['Algorithm'], 
                    autopct='%1.1f%%'
                )
                plt.title("Hit Ratio Distribution")
                st.pyplot(plt)
                plt.close()

            # Detailed Steps Expander
            with st.expander("🔍 Detailed Algorithm Steps"):
                for algo, steps in detailed_steps.items():
                    st.subheader(f"{algo} Algorithm Steps")
                    steps_df = pd.DataFrame(steps)
                    st.dataframe(steps_df)

    # Additional Information
    st.sidebar.markdown("### 💡 Algorithm Insights")
    st.sidebar.info("""
    - **FIFO**: Replaces the oldest page in memory
    - **LRU**: Replaces the least recently used page
    - **Optimal**: Replaces the page that won't be used for the longest time
    """)

def run():
    main()

if __name__ == "__main__":
    run()