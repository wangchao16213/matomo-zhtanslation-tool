import os,shutil
matomoDir = 'E:/workspaces/php_workspace/matomo/matomo'
pluginsPath = matomoDir + '/plugins/'
if __name__ == "__main__":
    plugins_names = os.listdir('./plugins')
    for plugins_name in plugins_names:
        if os.path.exists(pluginsPath + plugins_name):
            shutil.copyfile('./plugins/' + plugins_name + '/zh-cn.json',pluginsPath + plugins_name + '/zh-cn.json')
            
            

