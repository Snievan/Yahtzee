from typing import List

import numpy as np


class Dices:
    range_of_face: int = 6
    num_of_dices: int = 5

    faces: np.ndarray
    # def roll_dice

    # def __init__(self) -> None:
    #     self.faces = np.array()

    def __init__(self, faces: List = [1, 2, 3, 4, 5]):
        self.set_faces(faces)

    def as_array(self):
        pass

    def roll_partial(self, cur_faces: np.ndarray, select_dice: List[int]) -> np.ndarray:
        "Roll dices with partial selected"
        rand_dices = self.roll_all()
        for select in select_dice:
            cur_faces[select] = rand_dices[select]
        return cur_faces

    def roll_all(self) -> np.ndarray:
        "Roll all dices"
        rand_dices = np.random.randint(
            1, 1+self.range_of_face, size=self.num_of_dices)
        return rand_dices

    def __call__(self, select_dice: List[int] = None) -> None:
        """Dice rolls on calls"""
        if not select_dice:
            self.faces = self.roll_all()
        else:
            self.faces = self.roll_partial(self.faces,select_dice)

    def set_faces(self, faces: List):
        assert len(
            faces) == self.num_of_dices, f"Please input {self.num_of_dices} number of dices"
        self.faces = np.array(faces)

    @property
    def _sum(self):
        return sum(self.faces)

    @property
    def _dist(self):
        """
        Return the distribution of face numbers:
        For example: [1,5,5,3,3] -> [1,0,2,0,2,0]
        """
        dist = np.zeros(self.range_of_face)
        for face in self.faces:
            ind = face-1
            dist[ind] += 1
        return dist

    @property
    def _dist_sorted(self):
        "Sort the face distribution in reversed order"
        dist = self._dist
        return np.sort(dist)[::-1]

    @property
    def _max_dup(self):
        "Return max num of dupicated dice"
        return self._dist_sorted[0]

    @property
    def _max_straight_len(self):
        "Return max staight len of dices"
        max_len = 0
        cur_len = 0
        for face_cnt in self._dist:
            if face_cnt:
                cur_len += 1
                max_len = max(max_len, cur_len)
            else:
                cur_len = 0
        return max_len

    # def __call__(self,) -> Any:
    #     pass

    def __repr__(self):
        return "-".join([str(int(i)) for i in self.faces])
