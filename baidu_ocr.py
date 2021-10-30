# python 3.5
# 百度tesseract-ocr使用
import os.path
from pdf2image import convert_from_path
from aip import AipOcr

#from aip import AipImageClassify

""" API """
#replace with your key
APP_ID = 'xxxx'
API_KEY = 'xxxx'
SECRET_KEY = 'xxxx'

# 初始化AipFace对象
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
#client = AipImageClassify(APP_ID, API_KEY, SECRET_KEY)

""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

def img_to_str(image_path, txt_path):
    """ 可选参数 """
    options = {}
    options["language_type"] = "CHN_ENG"  # 中英文混合
    options["detect_direction"] = "true"  # 检测朝向
    options["detect_language"] = "true"  # 是否检测语言
    options["probability"] = "false"  # 是否返回识别结果中每一行的置信度

    image = get_file_content(image_path)

    """ 带参数调用通用文字识别 """
    result = client.basicGeneral(get_file_content(filePath), options)

    # 格式化输出-提取需要的部分
    if 'words_result' in result:
        text = ('\n'.join([w['words'] for w in result['words_result']]))
    print(type(result), "和", type(text))

    """ save """
    fs = open(txt_path, 'w+')  # 将str,保存到txt
    fs.write(text)
    fs.close()
    return text

def pdf_to_png(fname):
    # 将pdf转换为png后，保存在f文件夹
    # pdf的名称就是放img的名称，每一页pdf是一张png
    f = fname.rsplit(".",1)[0]
    if not os.path.exists(f):
        os.mkdir(f)
    print("Start Converting PDF to PNG...")
    images = convert_from_path(fname, fmt="png", output_folder=f)
    print("Successfully converted!...")
    return images


def pdf_to_str(pdf_path, images):
    # images = pdf_to_png(pdf_path)
    pdf_name = pdf_path.rsplit(".", 1)[0]
    txt_path = pdf_name + ".txt"

    """ 可选参数 """
    options = {}
    options["language_type"] = "CHN_ENG"  # 中英文混合
    options["detect_direction"] = "true"  # 检测朝向
    options["detect_language"] = "true"  # 是否检测语言
    options["probability"] = "false"  # 是否返回识别结果中每一行的置信度

    txtfile = open(txt_path, 'w+')
    flag = 0
    for img in images:
        try:
            flag += 1
            print("Converting Page %d"%flag + "...")

            with open(img.filename, 'rb') as fimg:
                # 根据'PIL.PngImagePlugin.PngImageFile'对象的filename属性读取图片为二进制
                img = fimg.read()
            msg = client.basicGeneral(img)
            for i in msg.get('words_result'):
                txtfile.write('{}\n'.format(i.get('words')))
            txtfile.write('\f\n')
            print(f"第{flag}条用例执行成功")
        except Exception as e:
	        print(f"第{flag}条用例执行失败")
    txtfile.close()



if __name__ == '__main__':
    pdf_path = "xxx.pdf"
    images = pdf_to_png(pdf_path)
    pdf_to_str(pdf_path, images)

    print("识别完成。")



