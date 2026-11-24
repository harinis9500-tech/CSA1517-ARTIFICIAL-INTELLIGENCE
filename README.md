# CSA1517 — Artificial Intelligence Lab Experiments

All 50 assignments are organized into five day-wise folders. Each experiment has its own clearly named source file.

## Day 1
1. Eight-Puzzle Solver (A* Search) — `DAY_1/01_eight_puzzle_solver_a_search.py`
2. Eight-Queens Problem — `DAY_1/02_eight_queens_problem.py`
3. Water Jug Problem (BFS) — `DAY_1/03_water_jug_problem_bfs.py`
4. Cryptarithmetic: SEND + MORE = MONEY — `DAY_1/04_cryptarithmetic_send_more_money.py`
5. Missionaries and Cannibals — `DAY_1/05_missionaries_and_cannibals.py`
6. Vacuum Cleaner Agent — `DAY_1/06_vacuum_cleaner_agent.py`
7. Breadth First Search (BFS) — `DAY_1/07_breadth_first_search_bfs.py`
8. Depth First Search (DFS) — `DAY_1/08_depth_first_search_dfs.py`
9. Travelling Salesperson Problem — `DAY_1/09_travelling_salesperson_problem.py`
10. A* Search Algorithm — `DAY_1/10_a_search_algorithm.py`

## Day 2
11. Map Colouring using CSP — `DAY_2/11_map_colouring_using_csp.py`
12. Tic-Tac-Toe Game — `DAY_2/12_tic_tac_toe_game.py`
13. Minimax Algorithm — `DAY_2/13_minimax_algorithm.py`
14. Alpha-Beta Pruning — `DAY_2/14_alpha_beta_pruning.py`
15. Decision Tree Classifier — `DAY_2/15_decision_tree_classifier.py`
16. Feedforward Neural Network — `DAY_2/16_feedforward_neural_network.py`
17. Prolog: Sum of 1 to N — `DAY_2/17_prolog_sum_of_1_to_n.pl`
18. Prolog: Name and DOB Database — `DAY_2/18_prolog_name_and_dob_database.pl`
19. Prolog: Student-Teacher-Subject Database — `DAY_2/19_prolog_student_teacher_subject_database.pl`
20. Prolog: Planets Database — `DAY_2/20_prolog_planets_database.pl`

## Day 3
21. Prolog: Towers of Hanoi — `DAY_3/21_prolog_towers_of_hanoi.pl`
22. Prolog: Birds that Can Fly — `DAY_3/22_prolog_birds_that_can_fly.pl`
23. Prolog: Family Tree — `DAY_3/23_prolog_family_tree.pl`
24. Prolog: Diet Suggestion Rules — `DAY_3/24_prolog_diet_suggestion_rules.pl`
25. Prolog: Monkey and Banana Problem — `DAY_3/25_prolog_monkey_and_banana_problem.pl`
26. Prolog: Fruit and Colour Backtracking — `DAY_3/26_prolog_fruit_and_colour_backtracking.pl`
27. Prolog: Best-First Search — `DAY_3/27_prolog_best_first_search.pl`
28. Prolog: Medical Diagnosis Rules — `DAY_3/28_prolog_medical_diagnosis_rules.pl`
29. Prolog: Forward Chaining — `DAY_3/29_prolog_forward_chaining.pl`
30. Prolog: Backward Chaining — `DAY_3/30_prolog_backward_chaining.pl`

## Day 4
31. HTML Blog: Anchor and Title Tags — `DAY_4/31_html_blog_anchor_and_title_tags.html`
32. Linear Regression — `DAY_4/32_linear_regression.py`
33. K-Nearest Neighbours (KNN) — `DAY_4/33_k_nearest_neighbours_knn.py`
34. Image Classifier using TensorFlow — `DAY_4/34_image_classifier_using_tensorflow.py`
35. Decision Tree Classification — `DAY_4/35_decision_tree_classification.py`
36. Sentiment Analysis — `DAY_4/36_sentiment_analysis.py`
37. Genetic Algorithm: Function Optimisation — `DAY_4/37_genetic_algorithm_function_optimisation.py`
38. Support Vector Machine (SVM) — `DAY_4/38_support_vector_machine_svm.py`
39. Principal Component Analysis (PCA) — `DAY_4/39_principal_component_analysis_pca.py`
40. Collaborative Filtering Recommendation — `DAY_4/40_collaborative_filtering_recommendation.py`

## Day 5
41. NLP Rule-Based Chatbot — `DAY_5/41_nlp_rule_based_chatbot.py`
42. K-Means Clustering — `DAY_5/42_k_means_clustering.py`
43. Reinforcement Learning: Q-Learning — `DAY_5/43_reinforcement_learning_q_learning.py`
44. Image Segmentation using K-Means — `DAY_5/44_image_segmentation_using_k_means.py`
45. Markov Chain Simulation — `DAY_5/45_markov_chain_simulation.py`
46. Pretrained Object Detection — `DAY_5/46_pretrained_object_detection.py`
47. Hyperparameter Tuning — `DAY_5/47_hyperparameter_tuning.py`
48. Bayesian Network Inference — `DAY_5/48_bayesian_network_inference.py`
49. Pretrained Face Detection — `DAY_5/49_pretrained_face_detection.py`
50. Genetic Algorithm Evolving Neural Network — `DAY_5/50_genetic_algorithm_evolving_neural_network.py`


## Requirements and execution
- Python 3.9+ for `.py` files; SWI-Prolog for `.pl` files; a browser for the HTML page.
- Common packages: `numpy`, `scikit-learn`, `matplotlib`, `Pillow`, `opencv-python`, `tensorflow`, and `pgmpy`. Install only the dependency needed by a particular experiment.
- Image tasks require local input images named in the program. The pretrained object detector additionally requires MobileNet-SSD model files.
- Example: `python DAY_1/07_breadth_first_search_bfs.py`
- Open a Prolog file with `swipl -s path/to/file.pl`, then run the query shown in its comments.
- The diet and diagnosis programs are educational logic demonstrations, not medical advice.
