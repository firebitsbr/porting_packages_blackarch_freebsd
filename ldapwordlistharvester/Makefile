PORTNAME=	ldapwordlistharvester
DISTVERSION=	1.2.r18.g60c619d
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Tool to generate wordlist from information present in LDAP, in order to crack passwords of domain accounts.
WWW=		https://github.com/p0dalirius/pyLDAPWordlistHarvester

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-pycryptodome@${PY_FLAVOR} \
		??/py-sectools@${PY_FLAVOR} \
		??/py-xlsxwriter@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
