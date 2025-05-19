# How to Push Your Project to GitHub

This guide will help you push your Customer Management System project to your GitHub repository.

## Prerequisites
- You have already created a GitHub repository named "customer-management-system"
- You have a GitHub account
- Git is installed on your computer (already confirmed)

## Steps to Push Your Project to GitHub

### 1. Add the Remote Repository

Replace `YOUR_USERNAME` with your actual GitHub username in the following command:

```bash
git remote add origin https://github.com/YOUR_USERNAME/customer-management-system.git
```

For example, if your GitHub username is "johndoe", the command would be:

```bash
git remote add origin https://github.com/johndoe/customer-management-system.git
```

### 2. Push Your Code to GitHub

After adding the remote repository, push your code:

```bash
git push -u origin master
```

You may be prompted to authenticate with GitHub. Follow the instructions in your browser to complete the authentication.

## Verifying the Push

After pushing, you can visit your GitHub repository in a web browser to verify that your code has been uploaded:

```
https://github.com/YOUR_USERNAME/customer-management-system
```

## Making Future Changes

When you make changes to your project, follow these steps to update your GitHub repository:

1. Stage your changes:
   ```bash
   git add .
   ```

2. Commit your changes with a descriptive message:
   ```bash
   git commit -m "Description of the changes you made"
   ```

3. Push your changes to GitHub:
   ```bash
   git push
   ```

## Using SSH Instead of HTTPS (Optional)

If you prefer to use SSH instead of HTTPS for connecting to GitHub (which doesn't require entering your password each time), you can set it up by:

1. Generating an SSH key if you don't have one:
   ```bash
   ssh-keygen -t ed25519 -C "your.email@example.com"
   ```

2. Adding the SSH key to your GitHub account (in GitHub settings)

3. Changing your remote URL to use SSH:
   ```bash
   git remote set-url origin git@github.com:YOUR_USERNAME/customer-management-system.git
   ```

## Troubleshooting

If you encounter any issues:

- Make sure your GitHub repository exists and is spelled correctly
- Ensure you have the necessary permissions to push to the repository
- Check that your GitHub authentication is working properly