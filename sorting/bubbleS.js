function bubble_sort(arr){
    let n = arr.length
    for(let i=0; i < n; i++){
        let swapped = false
        for(let j=0; j < n-i-1; j++){
            if (arr[j] > arr[j+1]){
                let temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
                swapped = true
            }
        }
        if(!swapped){
            break
        }
    }
    return arr
}

let l = [2, 3, 9, 1, 6]
console.log(bubble_sort(l))