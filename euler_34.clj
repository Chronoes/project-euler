(ns euler)

(defn factorial [number]
  (loop [n number fact 1]
    (if (zero? n)
      fact
      (recur (dec n) (* fact n)))))

(defn digitsum? [nr]
  (= nr (reduce + (map factorial (map #(Character/digit % 10) (str nr))))))

(let [lim 22000000]
  (reduce + (filter digitsum? (range 2 lim))))
