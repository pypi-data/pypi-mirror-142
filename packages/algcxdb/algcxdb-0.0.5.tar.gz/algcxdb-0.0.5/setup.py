# -*- coding: gbk-*-
"""
* ���ߣ�������
* ʱ�䣺2022/1/25 14:00
* ���ܣ����Python��������ڷ�����pypi.org
* ˵�����뿴����.txt���ⷢ�����ʹ��ѧ��˼�����������
"""
import sys

from setuptools import setup,find_packages
#from xes import AIspeak

if __name__ == '__main__':
    sys.argv += ["sdist"]
setup(
    name='algcxdb',
    version='0.0.5',
    packages=find_packages(),
    url='https://alggfzslt.freeflarum.com/',
    license='MIT License',
    author='algfwq',
    author_email='3104374883@qq.com',
    description='������Ӳ���Ƽ������ҳ������⣡����',
    long_description='������Ӳ���Ƽ������ҳ������⣡����ʹ�ú���cxdb()���ɣ�����',
    requires=["pyinstaller"]
)


