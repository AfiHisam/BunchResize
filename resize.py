"""
Create by : AfiHisam
Date : 03042018
"""
import argparse
import os
from PIL import Image
from resizeimage import resizeimage

parser = argparse.ArgumentParser(description='Resize image')


parser.add_argument('-i', '--input', type=str, metavar='', required=True, help="Images location input")
parser.add_argument('-s', '--save', type=str, metavar='', required=True, help="Save location")

parser.add_argument('-w', '--width', type=int, metavar='', required=True, help="Images width")
parser.add_argument('-H', '--height', type=int, metavar='', required=True, help="Images height")

str1 = ''
args = parser.parse_args()

def resize(a,b,c,d):
	for filename in os.listdir(a):
		str1 = os.path.splitext(filename)[0]
		ext = os.path.splitext(filename)[1]

		with open(a+'/'+str1+ext, 'r+b') as f:  
			with Image.open(f) as image:
				cover = resizeimage.resize_cover(image, [c,d])
				cover.save(b+'/'+str1+ext, image.format)
				print('Resize :'+str1+ext)

if __name__ == '__main__':
	
	resize(args.input,args.save,args.width,args.height)
	
