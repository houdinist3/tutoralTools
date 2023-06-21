import os
import argparse
import binary




def main():
    """ Run polyReduceDemo"""
    parser = argparse.ArgumentParser(description='find assets and polyReduce them by a given amount')
    parser.add_argument('-d', '--dir', metavar='', default='', help='a dir to find assets')
    parser.add_argument('-a', '--amount', metavar='', default=50, help='amount to reduce asset by')   
    args = parser.parse_args()
    
    assetDir = args.dir
    amount = args.amount  
    
    if not assetDir and amount:
        print("need to supply dir and reduction amount")
        return

    print("assetDir : {}  amount : {}".format(assetDir, amount))
    
    command = 'hython -c "import sys; sys.path.append(\'D:/Git_Repo/tutoralTools/utils\');' 
    command += ' import houUtils; houUtils.runReduction(\'%s\',\'%s\')"' % (assetDir, amount)


    print(command)
    # command = '%s -c "import sys; sys.path.append(\'D:\\Git_Repo\\tutoralTools\\utils\');'
    # command += ' import houUtils; houUtils.runReduction(\'%s\',\'%s\')"' % (hython,assetDir, amount)
    os.system(command)
    
    print("reduction complete")

    
if __name__ == "__main__":
    main() 
