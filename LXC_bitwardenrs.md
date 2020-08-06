**Create**

Create, but don’t start the container

You’ll want 2+ cores for compiling, then drop to 1 once all done

Enable Start at Boot

Start container
```
apt update && apt upgrade -y && sed -i 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/g' /etc/locale.gen && locale-gen && localectl set-locale LANG=en_US.UTF-8 && set LC_ALL=en_US.UTF-8 && reboot now
```
```
apt install -y git wget curl nodejs npm build-essential pkg-config && curl https://sh.rustup.rs -sSf | sh && echo 'export PATH=~/.cargo/bin:$PATH' >> ~/.bashrc && export PATH=~/.cargo/bin:$PATH git clone https://github.com/dani-garcia/bitwarden_rs && pushd bitwarden_rs && cargo clean && cargo build --features sqlite --release && pushd target/release
```
Go here and pick the most recent release:
```
https://github.com/dani-garcia/bw_web_builds/releases wget <linkToRelease> && tar zxvf bw_web* mkdir /var/lib/bitwarden_rs
```
```
nano /etc/systemd/system/bitwarden.service (see below)
```
```
nano /etc/bitwarden_rs.env (see below)
```
**Bitwarden.service**
```
[Unit]
Description=Bitwarden Server (Rust Edition)
Documentation=https://github.com/dani-garcia/bitwarden_rs
After=network.target

[Service]
User=root
Group=root

EnvironmentFile=/etc/bitwarden_rs.env
ExecStart=/root/bitwarden_rs/target/release/bitwarden_rs

WorkingDirectory=/var/lib/bitwarden_rs
ReadWriteDirectories=/var/lib/bitwarden_rs
AmbientCapabilities=CAP_NET_BIND_SERVICE

[Install]
WantedBy=multi-user.target
```
**Bitwarden_rs.env**
```
WEB_VAULT_FOLDER=/root/bitwarden_rs/target/release/web-vault
WEB_VAULT_ENABLED=true
# Uncomment this once vaults restored
#SIGNUPS_ALLOWED=false

# vim: syntax=ini
```

Resources https://www.reddit.com/r/Bitwarden/comments/dg78bi/building_selfhosted_bitwarden_via_bitwarden_rs/ https://github.com/dani-garcia/bitwarden_rs/wiki/Setup-as-a-systemd-service

