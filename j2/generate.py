from jinja2 import Environment, FileSystemLoader
import os

# 设置Jinja2模板目录
template_dir = "j2"

# 创建Jinja2环境对象
env = Environment(loader=FileSystemLoader(template_dir))

# 定义要传递给模板的数据
data = {
    'name': 'John',
}

# 渲染模板
template = env.get_template('iam_6mlldap_log4j2.xml.j2')
output = template.render(data)

# 将生成的内容写入实际文件
with open('./j2/iam_6mlldap_log4j2.xml', 'w') as f:
    f.write(output)

print('生成成功！')