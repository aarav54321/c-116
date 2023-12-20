import cv2

# Read the image
img = cv2.imread("solar-system.jpg")

# Function to add text to the image
def add_text(image, text, position, font=cv2.FONT_HERSHEY_SIMPLEX, font_scale=1, color=(255, 255, 255), thickness=2):
    cv2.putText(image, text, position, font, font_scale, color, thickness, cv2.LINE_AA)

# Add text for each planet
add_text(img, "Sun", (0, 250), font_scale=0.8, color=(255, 255, 255))
add_text(img, "Mercury", (70, 190), font_scale=0.8, color=(255, 255, 255))
add_text(img, "Venus", (150, 250), font_scale=0.8, color=(255, 255, 255))
add_text(img, "Earth", (250, 250), font_scale=0.8, color=(255, 255, 255))
add_text(img, "Mars", (350, 250), font_scale=0.8, color=(255, 255, 255))
add_text(img, "Jupiter", (520, 250), font_scale=0.8, color=(255, 255, 255))
add_text(img, "Saturn", (770, 300), font_scale=0.8, color=(255, 255, 255))
add_text(img, "Uranus", (950, 300), font_scale=0.8, color=(255, 255, 255))
add_text(img, "Neptune", (1100, 300), font_scale=0.8, color=(255, 255, 255))

# Display the image
cv2.imshow("output", img)
cv2.waitKey(0)

# Save the final image
cv2.imwrite("Solar_system_with_name.jpg", img)

# Close all OpenCV windows
cv2.destroyAllWindows()