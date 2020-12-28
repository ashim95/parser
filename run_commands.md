- Train BiAffine Parser
```
python -m supar.cmds.biaffine_dependency train -b -d 0 -c config.ini -p models/sanskrit.biaffine.dependency.char/model -f char --train data/sanskrit/ud_format_no_tags/ud_pos_ner_dp_train_san --dev data/sanskrit/ud_format_no_tags/ud_pos_ner_dp_dev_san --test data/sanskrit/ud_format_no_tags/ud_pos_ner_dp_test_san  --tree
```

- Predicting
```
python -m supar.cmds.biaffine_dependency predict -p models/sanskrit.biaffine.dependency.char/model --data data/sanskrit/ud_format_no_tags/ud_pos_ner_dp_test_san  --tree --pred models/sanskrit.biaffine.dependency.char/test.preds
```

- Evaluating on test set
```
python -m supar.cmds.biaffine_dependency evaluate -p models/sanskrit.biaffine.dependency.char/model --data data/sanskrit/ud_format_no_tags/ud_pos_ner_dp_test_san  --tree
```
