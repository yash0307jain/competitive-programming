"use strict";
function insertionSort(arr) {
    for (let i = 1; i < arr.length; i++) {
        let key = arr[i];
        let j = i - 1;
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j = j - 1;
        }
        arr[j + 1] = key;
        console.log(arr);
    }
}
let arr = [6, 5, 3, 2, 8, 10, 9];
insertionSort(arr);
