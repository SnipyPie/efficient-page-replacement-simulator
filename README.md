# efficient-page-replacement-simulator
a simulator to simulate the page replacement algorithms
📌 Overview
This project is an interactive web-based simulator that visualizes and compares three fundamental page replacement algorithms used in operating systems:

FIFO (First-In-First-Out)

LRU (Least Recently Used)

Optimal Algorithm

Built with Python and Streamlit, the simulator provides an intuitive interface for students and developers to understand how different algorithms handle page faults under varying memory conditions.

✨ Features
🖥️ Interactive web interface using Streamlit

📊 Real-time visualization with bar charts and pie charts

📝 Step-by-step execution logs for each algorithm

🔢 Customizable inputs:

Page reference strings

Number of memory frames

📱 Responsive design (works on desktop browsers)

📈 Performance metrics comparison:

Page faults count

Hit/miss ratios

🛠️ Technologies Used
Python 3 (Core programming language)

Streamlit (Web application framework)

Matplotlib (Data visualization)

Pandas (Data handling and display)

NumPy (Numerical operations)

🚀 Getting Started
Prerequisites
Python 3.7 or higher

pip package manager

Installation
Clone the repository:

bash
git clone https://github.com/your-username/page-replacement-simulator.git
cd page-replacement-simulator
Install required packages:

bash
pip install -r requirements.txt
Running the Application
bash
streamlit run efficient_page_replacement.py
The application will automatically open in your default web browser at http://localhost:8501

🧮 How to Use
Input Parameters (Left Sidebar):

Enter your page reference string (space-separated numbers)

Select number of frames using the slider

Choose which algorithms to simulate

Run Simulation:

Click the "🚀 Run Simulation" button

View Results:

Performance metrics table

Comparative bar chart of page faults

Pie chart showing hit ratios

Detailed step-by-step execution for each algorithm

📚 Algorithm Details
FIFO (First-In-First-Out)
Replaces the oldest page in memory

Simple implementation but may suffer from Belady's Anomaly

LRU (Least Recently Used)
Replaces the page that hasn't been used for the longest time

Better performance than FIFO but requires more overhead

Optimal Algorithm
Replaces the page that won't be used for the longest time in future

Provides theoretical best performance (but impractical in real systems)

📈 Performance Comparison Example
Input:

Reference String: 7 0 1 2 0 3 0 4

Frames: 3

Results:

Algorithm	Page Faults	Hit Ratio
FIFO	6	25%
LRU	5	37.5%
Optimal	4	50%
🌟 Future Enhancements
Add more algorithms (MRU, Clock, Second Chance)

Implement animated page replacement visualization

Add mobile-responsive design improvements

Export results as PDF/CSV functionality

Dark mode support

🤝 Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements.

Fork the project

Create your feature branch (git checkout -b feature/AmazingFeature)

Commit your changes (git commit -m 'Add some AmazingFeature')

Push to the branch (git push origin feature/AmazingFeature)

Open a Pull Request

📜 License
Distributed under the MIT License. See LICENSE for more information.

📧 Contact
Project Link: https://github.com/your-username/page-replacement-simulator

🙏 Acknowledgments
Inspired by Operating System concepts from "Operating System Concepts" by Silberschatz, Galvin, and Gagne

Streamlit documentation for UI components

GeeksforGeeks for algorithm references
