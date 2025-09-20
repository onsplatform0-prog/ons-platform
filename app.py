from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # For flash messages

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/articles')
def articles():
    return render_template('articles.html')

@app.route('/tests', methods=['GET', 'POST'])
def tests():
    if request.method == 'POST':
        # Simple stress assessment logic
        q1 = request.form.get('q1', '0')
        q2 = request.form.get('q2', '0')
        q3 = request.form.get('q3', '0')
        
        total_score = int(q1) + int(q2) + int(q3)
        
        if total_score <= 3:
            result = "منخفض"
            message = "ممتاز! يبدو أنك تدير التوتر بشكل جيد. استمر في العمل الجيد!"
        elif total_score <= 6:
            result = "متوسط"
            message = "أنت تعاني من توتر معتدل. فكر في بعض تقنيات الاسترخاء."
        else:
            result = "عالي"
            message = "أنت تعاني من مستويات عالية من التوتر. يرجى التفكير في طلب الدعم."
        
        flash(f"مستوى التوتر لديك: {result}. {message}", 'result')
        return redirect(url_for('tests'))
    
    return render_template('tests.html')

@app.route('/chatbot')
def chatbot():
    return render_template('chatbot.html')

@app.route('/login')
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
