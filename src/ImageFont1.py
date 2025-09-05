from PIL import Image, ImageDraw, ImageFont
im = Image.new('RGBA',(200,200),'white')
draw = ImageDraw.Draw(im)
# MS P明朝
jfont = ImageFont.truetype('msmincho.ttc',24,index=1)
draw.text((20,20),'こんにちは',fill='black',font=jfont)
# MS Pゴシック
jfont = ImageFont.truetype('msgothic.ttc',24,index=2)
draw.text((20,50),'こんにちは',fill='black',font=jfont)
# メイリオ
jfont = ImageFont.truetype('meiryo.ttc',24,index=0)
draw.text((20,80),'こんにちは',fill='black',font=jfont)
# BIZ UDPゴシック
jfont = ImageFont.truetype('BIZ-UDGothicR.ttc',24,index=1)
draw.text((20,110),'こんにちは',fill='black',font=jfont)
# BIZ UDP明朝 Medium
jfont = ImageFont.truetype('BIZ-UDMinchoM.ttc',24,index=1)
draw.text((20,140),'こんにちは',fill='black',font=jfont)
im.save('jtext.png')
