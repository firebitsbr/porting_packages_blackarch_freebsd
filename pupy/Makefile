PORTNAME=	pupy
DISTVERSION=	2988.4b78dc58
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Opensource, cross-platform (Windows, Linux, OSX, Android) remote administration and post-exploitation tool mainly written in python.
WWW=		https://github.com/n1nj4sec/pupy

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		ftp/wget

RUN_DEPENDS=	??/impacket \
		??/libffi \
		??/py-cerberus@${PY_FLAVOR} \
		??/py-colorama@${PY_FLAVOR} \
		??/py-dateparser@${PY_FLAVOR} \
		??/py-defusedxml@${PY_FLAVOR} \
		??/py-dnslib@${PY_FLAVOR} \
		??/py-ecdsa@${PY_FLAVOR} \
		??/py-filemagic@${PY_FLAVOR} \
		??/py-flake8-per-file-ignores@${PY_FLAVOR} \
		??/py-flake8@${PY_FLAVOR} \
		??/py-fuse@${PY_FLAVOR} \
		??/py-hexdump@${PY_FLAVOR} \
		??/py-http-parser@${PY_FLAVOR} \
		??/py-keyboard@${PY_FLAVOR} \
		??/py-logutils@${PY_FLAVOR} \
		??/py-m2crypto@${PY_FLAVOR} \
		??/py-msgpack@${PY_FLAVOR} \
		??/py-mss@${PY_FLAVOR} \
		??/py-netaddr@${PY_FLAVOR} \
		??/py-netifaces@${PY_FLAVOR} \
		??/py-paramiko@${PY_FLAVOR} \
		??/py-pefile@${PY_FLAVOR} \
		??/py-poster@${PY_FLAVOR} \
		??/py-psutil@${PY_FLAVOR} \
		??/py-puttykeys@${PY_FLAVOR} \
		??/py-pyaes@${PY_FLAVOR} \
		??/py-pyaml@${PY_FLAVOR} \
		??/py-pycryptodome@${PY_FLAVOR} \
		??/py-pyelftools@${PY_FLAVOR} \
		??/py-pygments@${PY_FLAVOR} \
		??/py-pylzma@${PY_FLAVOR} \
		??/py-pyopenssl@${PY_FLAVOR} \
		??/py-pypykatz@${PY_FLAVOR} \
		??/py-pyuv@${PY_FLAVOR} \
		??/py-regex@${PY_FLAVOR} \
		??/py-rpyc@${PY_FLAVOR} \
		??/py-rsa@${PY_FLAVOR} \
		??/py-scandir@${PY_FLAVOR} \
		??/py-secretstorage@${PY_FLAVOR} \
		??/py-tinyec@${PY_FLAVOR} \
		??/py-tornado@${PY_FLAVOR} \
		??/py-tzlocal@${PY_FLAVOR} \
		??/py-win_inet_pton@${PY_FLAVOR} \
		??/py-xattr@${PY_FLAVOR} \
		??/tcpdump \
		lang/python \
		net/py-scapy@${PY_FLAVOR} \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
