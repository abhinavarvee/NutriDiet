import streamlit as st

def show_home():
    # st.markdown(
    #     """
    #     <style>
    #     .content-box {
    #         background-color: #f9f9f9;
    #         border: 1px solid #e0e0e0;
    #         border-radius: 10px;
    #         box-shadow: 0 4px 20px rgba(0, 128, 128, 0.4);
    #         padding: 20px;
    #         margin: 20px 0;
    #         position: relative;
    #         overflow: hidden;
    #     }
    #     .content-box::before {
    #         content: '';
    #         position: absolute;
    #         top: 0;
    #         left: 0;
    #         width: 100%;
    #         height: 100%;
    #         background: linear-gradient(45deg, rgba(255, 255, 255, 0.3), rgba(0, 128, 128, 0.3));
    #         opacity: 0.6;
    #         z-index: -1;
    #         transition: opacity 0.5s;
    #     }
    #     .content-box:hover::before {
    #         opacity: 1;
    #     }
    #     </style>
    #     """,
    #     unsafe_allow_html=True,
    # )

    st.markdown('<div class="content-box">', unsafe_allow_html=True)
    st.subheader("Why Follow a Diet Plan?")
    st.write("""
    Maintaining a balanced diet is crucial for overall health and well-being. Here are some reasons why you should consider following a diet plan:
    - **Weight Management**: A structured diet helps in maintaining a healthy weight by providing the right balance of nutrients.
    - **Nutritional Balance**: Ensures you get all the essential nutrients, vitamins, and minerals your body needs.
    - **Energy Levels**: Proper nutrition keeps your energy levels stable throughout the day.
    - **Disease Prevention**: A healthy diet can help prevent chronic diseases such as diabetes, heart disease, and obesity.
    - **Mental Health**: Good nutrition is linked to better mental health and reduced stress levels.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="content-box">', unsafe_allow_html=True)
    st.subheader("Benefits of a Personalized Diet Plan")
    st.write("""
    Personalized diet plans offer tailored recommendations based on your individual needs. Here are the benefits:
    - **Customization**: Diet plans are tailored to your age, weight, height, and activity level.
    - **Flexibility**: Adjustments can be made based on your preferences and lifestyle.
    - **Sustainability**: Easier to stick to compared to generic diets, leading to long-term success.
    - **Targeted Goals**: Helps you achieve specific health goals, whether it's weight loss, muscle gain, or improved overall health.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="content-box">', unsafe_allow_html=True)
    st.subheader("How Our App Helps You")
    st.write("""
    Our Diet Recommendation App uses advanced algorithms to provide you with personalized diet plans. Here's what you can expect:
    - **Ease of Use**: Simple interface to input your details and get recommendations.
    - **Data Tracking**: Keep track of your food intake and monitor your progress.
    - **Expert Guidance**: Recommendations based on scientific research and expert advice.
    - **Continuous Improvement**: Regular updates and improvements based on user feedback and the latest nutritional science.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="content-box">', unsafe_allow_html=True)
    st.subheader("Additional Tips for a Healthy Diet")
    st.write("""
    In addition to following a personalized diet plan, consider these tips for maintaining a healthy diet:
    - **Stay Hydrated**: Drink plenty of water throughout the day to stay hydrated.
    - **Eat a Variety of Foods**: Include a variety of fruits, vegetables, whole grains, and lean proteins in your diet.
    - **Limit Processed Foods**: Minimize the intake of processed and sugary foods.
    - **Mindful Eating**: Pay attention to your hunger and fullness cues, and avoid eating out of boredom.
    - **Regular Exercise**: Combine a healthy diet with regular physical activity for optimal health.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="content-box">', unsafe_allow_html=True)
    st.subheader("Join Our Community")
    st.write("""
    Connect with others on their health journey by joining our community:
    - **Support Groups**: Participate in our online support groups to share experiences and tips.
    - **Weekly Challenges**: Engage in weekly health challenges to stay motivated.
    - **Expert Webinars**: Attend webinars hosted by nutrition and fitness experts.
    - **Success Stories**: Read and share success stories to inspire and be inspired.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

show_home()
