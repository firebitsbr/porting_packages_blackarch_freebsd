PORTNAME=	objection
DISTVERSION=	1.12.3
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Instrumented Mobile Pentest Framework.
WWW=		https://pypi.org/project/objection/#files

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-build@${PY_FLAVOR} \
		??/py-installer@${PY_FLAVOR} \
		??/py-wheel@${PY_FLAVOR} \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-click@${PY_FLAVOR} \
		??/py-delegator.py@${PY_FLAVOR} \
		??/py-flask@${PY_FLAVOR} \
		??/py-frida-tools@${PY_FLAVOR} \
		??/py-frida@${PY_FLAVOR} \
		??/py-litecli@${PY_FLAVOR} \
		??/py-packaging@${PY_FLAVOR} \
		??/py-pexpect@${PY_FLAVOR} \
		??/py-prompt_toolkit@${PY_FLAVOR} \
		??/py-pygments@${PY_FLAVOR} \
		??/py-semver@${PY_FLAVOR} \
		??/py-sqlparse@${PY_FLAVOR} \
		??/py-tabulate@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
