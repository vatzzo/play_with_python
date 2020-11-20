import logging

logging.basicConfig(level=logging.ERROR, format='%(levelname)-10s %(message)s')


class Matrix:
    def __init__(
        self, matrix_dimension, rows=0
    ):
        self.matrix_dimension = matrix_dimension

        if rows == 0:
            self.rows = [[0]*matrix_dimension for i in range(matrix_dimension)]
        else:
            self.rows = []
            for i in rows:
                if len(i) == matrix_dimension:
                    self.rows.append(i)
                else:
                    self.rows = []
                    logging.error("Wrong row dimension! It must has {itm} items instead of {itm_has}.".format(
                        itm=matrix_dimension, itm_has=len(i)))
                    break

    def _get_columns(self):
        column = []
        columns = []
        for i in range(self.matrix_dimension):
            for j in range(self.matrix_dimension):
                column.append(self.rows[j][i])
            columns.append(column)
            column = []
        return columns

    def __setitem__(
        self, index, item
    ):
        if len(item) == self.matrix_dimension:
            self.rows[index] = item
        else:
            logging.error("Wrong row dimension! It must has {itm} items. Matrix has not been changed.".format(
                itm=self.matrix_dimension))

    def __getitem__(
        self, index
    ):
        return self.rows[index]

    def __str__(self):
        str1 = ''
        for i in self.rows:
            for x in i:
                str1 = str1 + str(x) + ' '
            str1 += '\n'
        return str1

    def __add__(
        self, matrix
    ):
        matrix_res = Matrix(self.matrix_dimension)
        if type(matrix) == Matrix:
            for i in range(self.matrix_dimension):
                for j in range(self.matrix_dimension):
                    matrix_res[i][j] = self.rows[i][j] + matrix[i][j]
            return matrix_res
        elif type(matrix) in [int, float]:
            matrix_new = Matrix(self.matrix_dimension)
            matrix_new.fill_with(matrix)
            for i in range(self.matrix_dimension):
                for j in range(self.matrix_dimension):
                    matrix_res[i][j] = self.rows[i][j] + matrix_new[i][j]
            return matrix_res
        else:
            logging.error(
                "Wrong element of addition. It must be a number. Matrix has not been changed.")

    def __sub__(
        self, matrix
    ):
        matrix_res = Matrix(self.matrix_dimension)
        if type(matrix) == Matrix:
            for i in range(self.matrix_dimension):
                for j in range(self.matrix_dimension):
                    matrix_res[i][j] = self.rows[i][j] - matrix[i][j]
            return matrix_res
        elif type(matrix) in [int, float]:
            matrix_new = Matrix(self.matrix_dimension)
            matrix_new.fill_with(matrix)
            for i in range(self.matrix_dimension):
                for j in range(self.matrix_dimension):
                    matrix_res[i][j] = self.rows[i][j] - matrix_new[i][j]
            return matrix_res
        else:
            logging.error(
                "Wrong element of addition. It must be a number. Matrix has not been changed.")

    def __mul__(
        self, number
    ):
        matrix_res = Matrix(self.matrix_dimension)
        for i in range(self.matrix_dimension):
            for j in range(self.matrix_dimension):
                matrix_res[i][j] = self.rows[i][j] * number
        return matrix_res

    def __rmul__(
        self, number
    ):
        return self * number

    def __truediv__(
        self, number
    ):
        matrix_res = Matrix(self.matrix_dimension)
        for i in range(self.matrix_dimension):
            for j in range(self.matrix_dimension):
                matrix_res[i][j] = self.rows[i][j] / number
        return matrix_res

    def __matmul__(
        self, matrix
    ):
        matrix_res = Matrix(self.matrix_dimension)
        columns = matrix._get_columns()
        for i in range(self.matrix_dimension):
            for j in range(self.matrix_dimension):
                matrix_res[i][j] = sum([item[0]*item[1]
                                        for item in zip(self.rows[i], columns[j])])
        return matrix_res

    def __radd__(
        self, matrix
    ):
        return self + matrix

    def __rsub__(
        self, matrix
    ):
        if type(matrix) in [int, float]:
            matrix_new = Matrix(self.matrix_dimension)
            matrix_new.fill_with(matrix)
            return matrix_new - self
        else:
            logging.error(
                "Wrong element of addition. It must be a number. Matrix has not been changed.")

    def fill_with(
        self, number
    ):
        for i in range(self.matrix_dimension):
            for j in range(self.matrix_dimension):
                self.rows[i][j] = number


if __name__ == "__main__":
    m1 = Matrix(3)
    m1[0] = [1, 2, 3]
    m1[1] = [1, 2, 3]
    m1[2] = [1, 2, 3]
    print(
        "Creation of matrix filled with zeros. Then setting particular rows ( m[row] ):\n{}".format(m1))

    m2 = Matrix(3, [[5, 2, 5], [5, 2, 5], [5, 2, 5]])
    print(
        "Creation of matrix by passing rows as arguments in constructor function:\n{}".format(m2))

    m3 = m1 + m2
    print(
        "Result of addition of 2 matrices:\n{}".format(m3))

    m3 = m1 - m2
    print(
        "Result of subtraction of 2 matrices:\n{}".format(m3))

    m3 = m1 * 2
    print(
        "Result of multiplication of matrix by 2:\n{}".format(m3))

    m3 = m1 / 2
    print(
        "Result of division of matrix by 2:\n{}".format(m3))

    m3 = m1 @ m2
    print(
        "Result of multiplication of 2 matrices:\n{}".format(m3))

    print("Iterator: ")
    for i in m3:
        print(i)
    print("\n")

    m3 = m1 + 2
    print(
        "Result of addition (m1 + 2):\n{}".format(m3))

    m3 = 2 + m1
    print(
        "Result of addition (2 + m1):\n{}".format(m3))

    m3 = m1 - 2
    print(
        "Result of subtraction (m1 - 2):\n{}".format(m3))

    m3 = 2 - m1
    print(
        "Result of subtraction (2 - m1):\n{}".format(m3))
