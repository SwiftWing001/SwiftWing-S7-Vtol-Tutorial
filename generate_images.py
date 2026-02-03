import requests
import os

# 图片保存目录
image_dir = r"d:\Users\cyx20\Documents\SwiftWing-S7-Vtol-Tutorial\docs\快速上手\image\完整飞行演示"

# 确保目录存在
os.makedirs(image_dir, exist_ok=True)

# 图片列表和对应的描述
image_list = [
    ("1767517162714.png", "SwiftWing S7 VTOL drone ready for flight with battery installed and propellers attached"),
    ("1767518412448.png", "QGroundControl interface showing EKF2 reset command for SwiftWing S7 VTOL"),
    ("1767519409358.png", "QGroundControl status bar showing GPS satellite information and positioning data"),
    ("1767519459456.png", "QGroundControl satellite accuracy indicator showing less than 2 meters accuracy"),
    ("1767519757367.png", "Terminal window showing mavros swing.launch command execution for SwiftWing S7"),
    ("1767520978542.png", "Terminal window showing plane_circle_track.launch command execution"),
    ("1767593536826.png", "Terminal output showing current flight mode for SwiftWing S7 VTOL"),
    ("1767521723948.png", "SwiftWing S7 VTOL drone taking off in multicopter mode"),
    ("1767523343428.png", "QGroundControl showing POSCTL flight mode status for SwiftWing S7"),
    ("1767524102717.png", "SwiftWing S7 VTOL flying in fixed-wing mode following circular trajectory"),
    ("1767579560914.png", "Terminal window showing control program termination with 'done' message"),
    ("1767594710868.png", "Control program terminal output showing successful completion"),
    ("1767579962486.png", "Terminal window showing plane_circle_track.launch command for inclined circle flight"),
    ("1767596914661.png", "SwiftWing S7 VTOL flying in inclined circular trajectory with altitude changes"),
    ("1767581377118.png", "QGroundControl flight data showing altitude changes during circular flight"),
    ("1767579560914.png", "Terminal window showing control program termination with 'done' message"),
    ("1767595324753.png", "Control program terminal output showing successful completion"),
    ("1767584103258.png", "Terminal window showing plane_poly_track.launch command for figure-eight flight"),
    ("1767596901361.png", "QGroundControl showing POSCTL flight mode status for figure-eight flight"),
    ("1767583712863.png", "SwiftWing S7 VTOL positioning for figure-eight flight entry"),
    ("1767584228370.png", "SwiftWing S7 VTOL flying figure-eight trajectory in fixed-wing mode"),
    ("1767584399540.png", "SwiftWing S7 VTOL landing in multicopter mode after completing flight mission")
]

# 生成图片
for image_name, prompt in image_list:
    # 生成图片的API URL
    api_url = f"https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt={prompt}&image_size=landscape_16_9"
    
    try:
        # 发送请求
        response = requests.get(api_url, timeout=30)
        
        # 检查响应状态
        if response.status_code == 200:
            # 保存图片
            image_path = os.path.join(image_dir, image_name)
            with open(image_path, 'wb') as f:
                f.write(response.content)
            print(f"Generated image: {image_name}")
        else:
            print(f"Failed to generate image {image_name}: {response.status_code}")
    except Exception as e:
        print(f"Error generating image {image_name}: {e}")

print("Image generation completed!")
