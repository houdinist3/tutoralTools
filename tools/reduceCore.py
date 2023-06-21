import sys
sys.path.append("D:/Git_Repo/tutoralTools/utils/")
import houUtils
import polyResuce
houUtils.runReduction()


command =  '/Applications/Houdini/Houdini18.0.287/Frameworks/Houdini.framework/Versions/Current/Resources/bin/'
command += 'hython -c "import sys; sys.path.append(\'/PATH/TO/tutorialTools/utils\');'
command += ' import houUtils; houUtils.runReduction(\'%s\',\'%s\')"' % (assetDir, amount)
os.system(command)