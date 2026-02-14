PORTNAME=	wafw00f
DISTVERSION=	909.acf6104
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Identify and fingerprint Web Application Firewall (WAF) products protecting a website.
WWW=		https://github.com/EnableSecurity/wafw00f

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-beautifulsoup4@${PY_FLAVOR} \
		??/py-httpretty@${PY_FLAVOR} \
		??/py-pluginbase@${PY_FLAVOR} \
		??/py-urllib3@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
