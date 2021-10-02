## GIT

#### Play your own GIT repository

1. sign up a new account at `https://github.com/` with your Google account.
2. create a SSH key in your AWS Cloud9. (ref: https://docs.github.com/en/authentication/connecting-to-github-with-ssh)

    2.1 generate new SSH key. `ssh-keygen -t ed25519 -C "your_email@example.com"`
    2.2 start ssh agent. `eval "$(ssh-agent -s)"`
    2.3 add ssh private key to agent. `ssh-add ~/.ssh/id_ed25519`

3. add new SSH key to GitHub.

    3.1 copy SSH public key in your clipboard. `cat ~/.ssh/id_ed25519.pub`
    3.2 add new SSH public in your account.
