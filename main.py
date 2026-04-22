import numpy as np
import cv2 as cv

if __name__ == "__main__":
    
    img = cv.imread("img/art.png")
    
    # guarantees the img is in black and white
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    # <20 dark -> darker >20 dark -> white
    _, th = cv.threshold(gray, 200, 255, cv.THRESH_BINARY_INV)

    cv.imwrite("img/art_th.jpg", th)

    # extract the contour of the image
    contours, hierarchy = cv.findContours(
        th, 
        cv.RETR_EXTERNAL, 
        cv.CHAIN_APPROX_SIMPLE
    )

    # original img in the end, make a copy to not modify the original img
    drawn = cv.drawContours(img.copy(), contours, -1, (100,100,0), 10)

    cv.imwrite("img/art_contour.jpg", drawn)

    art_contour = cv.imread("img/art_contour.jpg")


    # contours = sorted(contours, key=cv.contourArea, reverse=True)[:7]

    print(f"Encontrados {len(contours)} contornos.")

    medium_points_contours = []

    for contour in contours:
        sum_x = 0
        sum_y = 0
        n = len(contour)

        # Percorre cada ponto do contorno
        for point in contour:
            x, y = point[0]  # Extrai x e y do array [[x, y]]
            sum_x += x
            sum_y += y

        # Calcula as médias (Xmedio e Ymedio)
        x_medio = int(sum_x / n)
        y_medio = int(sum_y / n)

        medium_points_contours.append((x_medio, y_medio))

    print(f"Contorno com {n} pontos -> Centro: ({x_medio}, {y_medio})")

    print(f'Centros dos contornos: {medium_points_contours}')

    # Draw a small circle at the center of each contour
    
    img_with_centers = art_contour.copy()

    cv.imwrite("img/art_contour_centers.jpg", img_with_centers)

    for x_medio, y_medio in medium_points_contours:
        cv.circle(img_with_centers, (x_medio, y_medio), 5, (100, 100, 100), -1)




    # Find the distances between the centers
    # if they are small save art_contour[x_medio] and art_contour[x_medio2..], they are of similar colour
    # similar = [], different = []
    distances = []
    
    for x_medio, y_medio in medium_points_contours:
        print(f'Pixel color at ({x_medio}, {y_medio}): {art_contour[y_medio, x_medio]}')
        for x_medio2, y_medio2 in medium_points_contours:
            if (x_medio, y_medio) != (x_medio2, y_medio2):
                distances.append(np.sqrt( 
                    (art_contour[y_medio, x_medio][0] - art_contour[y_medio2, x_medio2][0])**2
                     + (art_contour[y_medio, x_medio][1] - art_contour[y_medio2, x_medio2][1])**2
                     + (art_contour[y_medio, x_medio][2] - art_contour[y_medio2, x_medio2][2])**2 ) )
    
    for d in distances:
        print(f'Distância entre centros: {d}')

    
    """

    # print(f'Contornos: {contours}')

    # filter the contours by area, only keep the ones with area > 200
    contours_filtered = []

    for contour in contours:
        #print(cv.contourArea(contour))
        if cv.contourArea(contour) > 200:
            contours_filtered.append(contour)

    drawn_filtered = cv.drawContours(img, contours_filtered, -1, (0,255,0))

    cv.imwrite("img/patent_contour_filtered.jpg", drawn_filtered)
    """