-- FileName    : color.lua
-- Author      : luzhlon
-- Description : 在终端输出各种颜色
-- LastChange  : 2017/2/17

local fgcolor = {
    ['黑'] = 30,
    ['红'] = 31,
    ['绿'] = 32,
    ['黄'] = 33,
    ['蓝'] = 34,
    ['紫'] = 35,
    ['天'] = 36,
    ['白'] = 37
}
local bgcolor = {
    ['黑'] = 40,
    ['红'] = 41,
    ['绿'] = 42,
    ['黄'] = 43,
    ['蓝'] = 44,
    ['紫'] = 45,
    ['天'] = 46,
    ['白'] = 47
}
local function colorstr(str, fg, bg)
    return [[\033[%d;%dm%s\033[0m]]:format(bg,fg,str)
end
local function quote(str)
    return '"'..str..'"'
end
local exe = os.execute
exe 'echo -n "    "'
local whitb = bgcolor['白']
for k,v in pairs(fgcolor) do
    exe('echo -n '..quote(colorstr(k..v, v, whitb)))
end
print ''
local whitf = fgcolor['白']
for k,bg in pairs(bgcolor) do
    exe('echo -n '..quote(colorstr(k..bg, whitf, bg)))
    for k,fg in pairs(fgcolor) do
        exe('echo -n '..quote(colorstr('XXXX', fg, bg)))
    end
    print ''
end
--[[
## 代码解释如下
\33[0m 关闭所有属性
\33[1m 设置高亮度
\33[4m 下划线
\33[5m 闪烁
\33[7m 反显
\33[8m 消隐
\33[30m — \33[37m 设置前景色
\33[40m — \33[47m 设置背景色
\33[nA 光标上移n行
\33[nB 光标下移n行
\33[nC 光标右移n行
\33[nD 光标左移n行
\33[y;xH设置光标位置
\33[2J 清屏
\33[K 清除从光标到行尾的内容
\33[s 保存光标位置
\33[u 恢复光标位置
\33[?25l 隐藏光标
\33[?25h 显示光标
]]--
