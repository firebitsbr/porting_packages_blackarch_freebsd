PORTNAME=	mobsf
DISTVERSION=	v4.4.5.r0.g2b08dd0
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	An intelligent, all-in-one open source mobile application (Android/iOS) automated pen-testing framework capable of performing static, dynamic analysis and web API testing.
WWW=		https://github.com/MobSF/Mobile-Security-Framework-MobSF

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-setuptools-scm@${PY_FLAVOR} \
		devel/git \
		devel/py-pip@${PY_FLAVOR} \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/gunicorn \
		??/py-xmlsec@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
