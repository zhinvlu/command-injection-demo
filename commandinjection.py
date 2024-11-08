from flask import Flask, request, render_template_string
import os

app = Flask(__name__)

# 模板字符串，包含一个输入框和提交按钮
template = '''
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Command Injection Demo</title>
  </head>
  <body>
    <h1>命令注入 Demo</h1>
    <form method="post">
      <label for="command">Enter a command:</label>
      <input type="text" id="command" name="command">
      <button type="submit">Submit</button>
    </form>
    {% if result %}
      <h2>结果:</h2>
      <pre>{{ result }}</pre>
    {% endif %}
  </body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # 从表单中获取用户输入的命令
        user_command = request.form['command']
        
        # 直接在shell中执行用户输入的命令（这是非常危险的）
        # 注意：这是命令注入漏洞的关键部分
        result = os.popen(user_command).read()
        
        return render_template_string(template, result=result)
    return render_template_string(template)

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
