# webSearcher
A python script that outputs titles of random url's to a text document. The top level domain, the amount of urls and whether it is http or https, are defined by the user.

#### Syntax:
    python3 main.py amount request top-level-domain

### Example:

#### Input:
    python3 Coding/python/websiteSearcher/main.py 10 http:// .com

#### Output (console):
<div style="background-color:black;">
    <span style="color:purple">1</span>
    http://6988.com
    <span style="color:purple">2</span>
    http://4993.com
    <span style="color:purple">3</span>
    http://2197.com
    <span style="color:purple">4</span>
    http://4764.com
    <span style="color:purple">5</span>
    http://7665.com
    <span style="color:purple">6</span>
    http://835.com
    <span style="color:purple">7</span>
    http://2123.com
    <span style="color:purple">8</span>
    http://1931.com
    <span style="color:purple">9</span>
    http://7909.com
    <span style="color:purple">10</span>
    http://1104.com
</div>

#### Output (output.txt)
    http://1931.com [FORBIDDEN] 
    http://7909.com --> 请点击继续访问
    http://1104.com --> 抱歉，站点已暂停