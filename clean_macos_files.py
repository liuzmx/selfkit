#! python3
import os

def clean_macos_files(root: str):
    """清理路径下全部MacOS上.DS_Store和._开头文件"""

    names = os.listdir(root)
    for name in names:
        child = os.path.join(root, name)
        if name == r".DS_Store" or name == r"._.DS_Store":
            os.remove(child)
        elif name.startswith("._"):  # 删除._开头文件
            os.remove(child)
        elif os.path.isdir(os.path.join(root, name)):
            clean_macos_files(child)


if __name__ == "__main__":
    clean_macos_files(r"D:")
