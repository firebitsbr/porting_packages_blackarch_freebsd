PORTNAME=	frida-ios-dump
DISTVERSION=	53.56e99b2
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Pull decrypted ipa from jailbreak device.
WWW=		https://github.com/AloneMonkey/frida-ios-dump

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-argparse@${PY_FLAVOR} \
		??/py-bcrypt@${PY_FLAVOR} \
		??/py-cffi@${PY_FLAVOR} \
		??/py-colorama@${PY_FLAVOR} \
		??/py-enum34@${PY_FLAVOR} \
		??/py-frida-tools@${PY_FLAVOR} \
		??/py-idna@${PY_FLAVOR} \
		??/py-ipaddress@${PY_FLAVOR} \
		??/py-paramiko@${PY_FLAVOR} \
		??/py-prompt_toolkit@${PY_FLAVOR} \
		??/py-pyasn1@${PY_FLAVOR} \
		??/py-pycparser@${PY_FLAVOR} \
		??/py-pygments@${PY_FLAVOR} \
		??/py-pynacl@${PY_FLAVOR} \
		??/py-scp@${PY_FLAVOR} \
		??/py-tqdm@${PY_FLAVOR} \
		??/py-wcwidth@${PY_FLAVOR} \
		devel/py-six@${PY_FLAVOR} \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
