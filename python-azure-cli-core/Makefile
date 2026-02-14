PORTNAME=	python-azure-cli-core
DISTVERSION=	2.82.0
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Microsoft Azure Command-Line Tools Core Module.
WWW=		https://pypi.org/project/azure-cli-core/#files

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-adal@${PY_FLAVOR} \
		??/py-antlr4@${PY_FLAVOR} \
		??/py-argcomplete@${PY_FLAVOR} \
		??/py-azure-mgmt-resource@${PY_FLAVOR} \
		??/py-colorama@${PY_FLAVOR} \
		??/py-humanfriendly@${PY_FLAVOR} \
		??/py-jmespath@${PY_FLAVOR} \
		??/py-msrest@${PY_FLAVOR} \
		??/py-msrestazure@${PY_FLAVOR} \
		??/py-paramiko@${PY_FLAVOR} \
		??/py-pyaml@${PY_FLAVOR} \
		??/py-pygments@${PY_FLAVOR} \
		??/py-pyjwt@${PY_FLAVOR} \
		??/py-pyopenssl@${PY_FLAVOR} \
		??/py-pyperclip@${PY_FLAVOR} \
		??/py-tabulate@${PY_FLAVOR} \
		??/py-wheel@${PY_FLAVOR} \
		devel/py-six@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
