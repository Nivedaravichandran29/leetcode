// Last updated: 7/17/2026, 3:07:30 PM
class Solution {
    public String convertToTitle(int columnNumber) {
        StringBuilder result = new StringBuilder();

        while (columnNumber > 0) {
            columnNumber--; // Adjust for 1-based indexing
            char currentLetter = (char) ('A' + (columnNumber % 26));
            result.append(currentLetter);
            columnNumber /= 26;
        }

        return result.reverse().toString();
    }
}