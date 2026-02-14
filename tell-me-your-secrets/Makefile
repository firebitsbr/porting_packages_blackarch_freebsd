PORTNAME=	tell-me-your-secrets
DISTVERSION=	v2.4.2.r3.g5434b9d
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Find secrets on any machine from over 120 Different Signatures.
WWW=		https://github.com/valayDave/tell-me-your-secrets

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-build@${PY_FLAVOR} \
		??/py-wheel@${PY_FLAVOR} \
		devel/git \
		devel/py-pip@${PY_FLAVOR}

RUN_DEPENDS=	??/py-gitignore-parser@${PY_FLAVOR} \
		??/py-pandas@${PY_FLAVOR} \
		??/py-yaml@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
