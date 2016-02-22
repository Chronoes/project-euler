(ns euler)

(defn digitsum? [nr]
  (= nr (reduce + (map #(int (Math/pow % 5)) (map #(Character/digit % 10) (str nr))))))

(let [lim 354295]
  (reduce + (filter digitsum? (range 2 lim))))
