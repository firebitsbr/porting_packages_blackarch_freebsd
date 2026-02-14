PORTNAME=	qark
DISTVERSION=	301.ba1b265
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Tool to look for several security related Android application vulnerabilities.
WWW=		https://github.com/linkedin/qark

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		lang/python3

RUN_DEPENDS=	??/py-asn1crypto@${PY_FLAVOR} \
		??/py-certifi@${PY_FLAVOR} \
		??/py-cffi@${PY_FLAVOR} \
		??/py-chardet@${PY_FLAVOR} \
		??/py-click@${PY_FLAVOR} \
		??/py-cryptography@${PY_FLAVOR} \
		??/py-enum34@${PY_FLAVOR} \
		??/py-idna@${PY_FLAVOR} \
		??/py-ipaddress@${PY_FLAVOR} \
		??/py-javalang@${PY_FLAVOR} \
		??/py-jinja@${PY_FLAVOR} \
		??/py-markupsafe@${PY_FLAVOR} \
		??/py-pluginbase@${PY_FLAVOR} \
		??/py-pycparser@${PY_FLAVOR} \
		??/py-pyopenssl@${PY_FLAVOR} \
		??/py-urllib3@${PY_FLAVOR} \
		devel/py-setuptools@${PY_FLAVOR} \
		devel/py-six@${PY_FLAVOR} \
		lang/python3 \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
