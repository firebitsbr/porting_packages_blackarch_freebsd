PORTNAME=	python-ssh-mitm
DISTVERSION=	5.0.1
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	SSH mitm server for security audits supporting public key authentication, session hijacking and file manipulation.
WWW=		https://pypi.org/project/ssh-mitm/#files

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-build@${PY_FLAVOR} \
		??/py-wheel@${PY_FLAVOR} \
		devel/py-pip@${PY_FLAVOR}

RUN_DEPENDS=	??/py-colored@${PY_FLAVOR} \
		??/py-enhancements@${PY_FLAVOR} \
		??/py-packaging@${PY_FLAVOR} \
		??/py-paramiko@${PY_FLAVOR} \
		??/py-pyaml@${PY_FLAVOR} \
		??/py-pytz@${PY_FLAVOR} \
		??/py-rich@${PY_FLAVOR} \
		??/py-sshpubkeys@${PY_FLAVOR} \
		??/py-typeguard@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
