# Grid tmuxinator

Generate tmuxinator file which launch a grid of panes with a custom command

Usage:

```shell
python ssh_out_generator.py 16 --w_per_line 16 --template idiap_show_out_files.j2 > .tmuxinator.yml
tmuxinator --local
```
