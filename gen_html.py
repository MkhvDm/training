N = 10
mult_list = [[x*y for x in range(1,N+1)] for y in range(1,N+1)]

html_str = str('<html><body><table>')
for row in range(N):
    html_str += '<tr>'
    for col in range(N):
        value = str(mult_list[row][col])
        html_str += '<td><a href="http://'+ value +'.ru">' + value + '</a></td>'
    html_str += '</tr>'

html_str += '</table></body></html>'
print(html_str)