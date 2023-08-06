set -e -x

git clone {{ git_repo }} $HOME/composer

cd $HOME/composer

echo 'Checking out composer branch {{ git_branch }}'

git checkout {{ git_branch }}

pip install --user -e .[all]

composer -n {{ parameters['_n_gpus'] }} examples/run_composer_trainer.py -f /mnt/config/parameters.yaml
