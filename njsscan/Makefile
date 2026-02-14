PORTNAME=	njsscan
DISTVERSION=	0.3.1
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A static application testing (SAST) tool that can find insecure code patterns in your node.js applications.
WWW=		https://pypi.org/project/njsscan/#files

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-colorama@${PY_FLAVOR} \
		??/py-jschema-to-python@${PY_FLAVOR} \
		??/py-jsonpickle@${PY_FLAVOR} \
		??/py-libsast@${PY_FLAVOR} \
		??/py-pbr@${PY_FLAVOR} \
		??/py-ruamel-yaml@${PY_FLAVOR} \
		??/py-sarif-om@${PY_FLAVOR} \
		??/py-tabulate@${PY_FLAVOR} \
		??/semgrep \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
