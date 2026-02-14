PORTNAME=	truegaze
DISTVERSION=	117.c3f26bc
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Static analysis tool for Android/iOS apps focusing on security issues outside the source code.
WWW=		https://github.com/nightwatchcybersecurity/truegaze

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/androguard \
		??/py-asn1crypto@${PY_FLAVOR} \
		??/py-beautifultable@${PY_FLAVOR} \
		??/py-click@${PY_FLAVOR} \
		??/py-cryptography@${PY_FLAVOR} \
		??/py-jsonschema@${PY_FLAVOR} \
		??/py-pytest-cov@${PY_FLAVOR} \
		??/py-pytest@${PY_FLAVOR} \
		??/py-requests-mock@${PY_FLAVOR} \
		??/py-roca-detect@${PY_FLAVOR} \
		??/py-tldextract@${PY_FLAVOR} \
		??/py-toml@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
