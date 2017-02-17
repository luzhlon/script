-- FileName    : ss.lua
-- Author      : luzhlon
-- Description : 爬去shadowsocks帐号
-- LastChange  : 2017/2/17

os.execute 'rm index.html'
os.execute 'wget http://www.ishadowsocks.net/'
local f = io.open 'index.html'
local content = f:read '*a'

local function generate(alpha)
    local str =
            alpha..'服务器地址:(.-)<.-端口:(%d+)<.-'..
            alpha..'密码:(.-)<.-加密方式:(.-)<'

    local addr,port,passwd,method = content:match(str)
    --print(addr, port, passwd, method)

    local template = [[
{
    "server": "%s",
    "server_port": %s,
    "local_port": 8080,
    "password": "%s",
    "timeout":600,
    "method": "%s"
}
]]
    local f = io.open('ss'..alpha..'.json', 'w')
    f:write(template:format(addr, port, passwd, method))
    f:close()
end

generate('A')
generate('B')
generate('C')

f:close()
os.execute 'rm index.html'
