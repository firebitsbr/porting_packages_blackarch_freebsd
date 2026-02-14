PORTNAME=	python-artifacts
DISTVERSION=	20250913
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Digital Forensics Artifact Repository.
WWW=		https://pypi.org/project/artifacts/#files

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-mock@${PY_FLAVOR} \
		??/py-pbr@${PY_FLAVOR} \
		??/py-pyaml@${PY_FLAVOR} \
		??/py-yaml@${PY_FLAVOR} \
		devel/py-six@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
