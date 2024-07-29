s = """
• Designed and trained a 98% accurate Convolutional Neural Network (CNN) using TensorFlow/Keras to recognize alphanumeric characters from a diverse dataset
• Utilized OpenCV and NumPy for image preprocessing, extracting letters for CNN input
• Produced sophisticated data visualizations with Seaborn, Matplotlib, and OpenCV to effectively illustrate data and various outputs
"""

lines = s.split("\n")
for line in lines:
    line = line.replace("•", "").strip()
    if line:
        print("<li>" + line + "</li>")
