"""
Find the total area covered by two rectilinear rectangles in a 2D plane.

Each rectangle is defined by its bottom left corner and top right corner as
shown in the figure.

Rectangle Area
Assume that the total area is never beyond the maximum possible value of int.
"""


class Solution:
    # @param {integer} A
    # @param {integer} B
    # @param {integer} C
    # @param {integer} D
    # @param {integer} E
    # @param {integer} F
    # @param {integer} G
    # @param {integer} H
    # @return {integer}
    def computeArea(self, A, B, C, D, E, F, G, H):
        if C < E or G < A:
            return (G - E) * (H - F) + (C - A) * (D - B)
        if D < F or H < B:
            return (G - E) * (H - F) + (C - A) * (D - B)
        right = min(C, G)
        left = max(A, E)
        top = min(H, D)
        bottom = max(F, B)
        return (G - E) * (H - F) + (C - A) * (D - B) - \
               (right - left) * (top - bottom)
