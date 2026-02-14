PORTNAME=	stringsifter
DISTVERSION=	39.33c0cd5
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Machine learning tool that automatically ranks strings based on their relevance for malware analysis.
WWW=		https://github.com/fireeye/stringsifter

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-build@${PY_FLAVOR} \
		devel/git \
		devel/py-pip@${PY_FLAVOR}

RUN_DEPENDS=	??/py-joblib@${PY_FLAVOR} \
		??/py-numpy@${PY_FLAVOR} \
		??/py-scikit-learn@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
