# import streamlit as st
# from PIL import Image
# import utils
# import style

# st.title("PyTorch Style Transfer")
# image = st.sidebar.selectbox(
#     "Select image",
#     {"amber.jpg", 'cat_.jpg', 'robot_.jpg'}
# )

# style_name = st.sidebar.selectbox(
#     "Select Style",
#     ("candy", 'mosaic', 'rain-princess-cropped','rain-princess', 'udnie')
# )

# model= "C:/Users/A-Tech/Desktop/building_object_detection_using_YOLO/fast_neural_style_implementation/fast_neural_style/neural_style/saved_models/" + style_name + ".pth"
# input_image = "C:/Users/A-Tech/Desktop/building_object_detection_using_YOLO/fast_neural_style_implementation/fast_neural_style/neural_style/images/content-images/" + image
# output_image = "C:/Users/A-Tech/Desktop/building_object_detection_using_YOLO/fast_neural_style_implementation/fast_neural_style/neural_style/images/output-images/" + style_name + "-" + image

# st.write("### Source Image:")
# img = Image.open(input_image)
# st.image(img, width=400)

# clicked = st.button("Stylized")

# if clicked:
#     model = style.load_model(model)
#     style.stylize(model, input_image, output_image)

#     st.write('### Output image:')
#     image = Image.open(output_image)
#     st.image(image, width=400)

import streamlit as st
from PIL import Image
import style

st.title("PyTorch Style Transfer")
image = st.sidebar.selectbox(
    "Select image",
    ("amber.jpg", 'cat_.jpg')
)

style_name = st.sidebar.selectbox(
    "Select Style",
    ('candy', 'mosaic', 'rain_princess', 'udnie')
)

model_path = "neural_style/saved_models/" + style_name + ".pth"
input_image_path = "neural_style/images/content-images/" + image
output_image_path = "neural_style/images/output-images/" + style_name + "-" + image

st.write("### Source Image:")
img = Image.open(input_image_path)
st.image(img, width=400)

clicked = st.button("Stylized")

if clicked:
    st.write("Loading model...")
    style_model = style.load_model(model_path)

    st.write("Stylizing image...")
    style.stylize(style_model, input_image_path, output_image_path)

    st.write('### Output image:')
    output_img = Image.open(output_image_path)
    st.image(output_img, width=400)
