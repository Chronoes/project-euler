;; Anything you type in here will be executed
;; immediately with the results shown on the
;; right.

(ns euler)

(defn add [sum lim]
  (if (zero? lim)
    sum
    (let [n (inc (* 2 lim))]
      (add
       (+ sum (- (* 4 (* n n)) (* 12 lim)))
       (dec lim)))))

(defn add2 [sum lim]
  (if (zero? lim)
    sum
    (let [n (inc (* 2 lim))]
      (recur
       (+ sum (- (* 4 (* n n)) (* 12 lim)))
       (dec lim)))))

(let [lim (/ (dec 1001) 2)]
  (add 1 lim)
  (add2 1 lim))
