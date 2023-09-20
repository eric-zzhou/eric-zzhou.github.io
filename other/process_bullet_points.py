s = """
• Implemented various statistical methods and advanced machine learning models including Bollinger Bands, Support Vector Machines (SVMs), and Long Short-Term Memory (LSTM) networks to analyze and predict stock market trends
 • Utilized a comprehensive tech stack including Keras, Sklearn, Scipy, and NumPy for model development, alongside Matplotlib and Plotly for effective data visualization
 • Conducted in-depth research into parameter optimization, reading several research papers and exploring different combinations of technical indicators
 • Experimented with prediction outputs, examining price, change percentage, and direction as potential options and fine-tuning minimum confidence thresholds
 • Investigated stock clustering techniques based on research paper to group similar companies for more robust model training, learning about winsorizing of outliers in the process
 """

lines = s.split("\n")
for line in lines:
    line = line.replace("•", "").strip()
    if line:
        print("<li>" + line + "</li>")
