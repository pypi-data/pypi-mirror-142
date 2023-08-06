import cv2
import numpy
from numpy import ndarray
from injectable import injectable


@injectable
class UtilsOpencv:
    def get_dimensions_hw(self, image_cv: ndarray) -> (int, int):
        h, w = image_cv.shape[:2]
        return h, w

    def get_dimensions_wh(self, image_cv: ndarray) -> (int, int):
        h, w = image_cv.shape[:2]
        return w, h

    def get_number_of_channels(self, image_cv: ndarray) -> int:
        if image_cv.ndim == 2:
            return 1
        elif image_cv.ndim == 3:
            return image_cv.shape[-1]
        else:
            raise ValueError("Weird image with ndim=" + str(image_cv.ndim))

    def are_images_equal(self, image_cv_a: ndarray, image_cv_b: ndarray) -> bool:
        if image_cv_a.shape == image_cv_b.shape:
            difference = cv2.subtract(image_cv_a, image_cv_b)
            b, g, r = cv2.split(difference)
            if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
                return True
            else:
                return False
        else:
            return False

    def convert_to_grayscale(self, image_cv: ndarray) -> ndarray:
        if self.get_number_of_channels(image_cv) == 1:
            return image_cv
        else:
            return cv2.cvtColor(image_cv, cv2.COLOR_BGR2GRAY)

    def blur_gaussian(self, image_cv: ndarray, blur_x: int, blur_y: int) -> ndarray:
        new_image_cv = image_cv.copy()
        new_image_cv = cv2.GaussianBlur(new_image_cv, (blur_x, blur_y), 0)
        return new_image_cv

    # Image transformations
    #-------------------------------------------------------------------------------------------------------------------
    # Rotate (preserving original dimensions of the image)
    def rotate_bound(self, image_cv: ndarray, angle: float) -> ndarray:
        if angle == 0:
            return image_cv
        image_result = image_cv.copy()
        h, w = image_result.shape[:2]
        c_x, c_y, = (w // 2, h // 2)
        rotation_matrix = cv2.getRotationMatrix2D((c_x, c_y), angle, 1.0)
        image_result = cv2.warpAffine(image_result, rotation_matrix, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
        return image_result

    # Rotate (changing dimensions of the original image)
    def rotate_free(self, image_cv: ndarray, angle: float) -> ndarray:
        if angle == 0:
            return image_cv
        image_result = image_cv.copy()
        h, w = image_result.shape[:2]
        c_x, c_y, = (w // 2, h // 2)

        # Compute the rotation matrix
        rotation_matrix = cv2.getRotationMatrix2D((c_x, c_y), angle, 1.0)
        rotation_matrix_cos = numpy.abs(rotation_matrix[0, 0])
        rotation_matrix_sin = numpy.abs(rotation_matrix[0, 1])

        # Compute the new bounding dimensions of the image
        new_w = int((h * rotation_matrix_sin) + (w * rotation_matrix_cos))
        new_h = int((h * rotation_matrix_cos) + (w * rotation_matrix_sin))

        # Adjust the rotation matrix to take into account translation
        rotation_matrix[0, 2] += (new_w / 2) - c_x
        rotation_matrix[1, 2] += (new_h / 2) - c_y

        # Rotate
        image_result = cv2.warpAffine(image_result, rotation_matrix, (new_w, new_h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
        return image_result

    # Rotate (smartly, deciding which way of rotation will work better here)
    def rotate(self, image_cv: ndarray, angle: float, rotate_bound_threshold_angle: float = 20.0) -> ndarray:
        if -1.0 * rotate_bound_threshold_angle <= angle <= rotate_bound_threshold_angle:
            return self.rotate_bound(image_cv, angle)
        else:
            return self.rotate_free(image_cv, angle)
    #-------------------------------------------------------------------------------------------------------------------
