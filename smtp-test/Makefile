PORTNAME=	smtp-test
DISTVERSION=	6.151f636
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Automated testing of SMTP servers for penetration testing.
WWW=		https://github.com/isaudits/smtp-test

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/cutycapt \
		??/py-configparser@${PY_FLAVOR} \
		??/py-dnspython@${PY_FLAVOR} \
		lang/python3 \
		security/nmap


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
